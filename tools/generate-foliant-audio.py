"""Generate the complete local Piper phrase library after collect-foliant-speech.cjs."""
import argparse
import json
import multiprocessing
import subprocess
import tempfile
import wave
from pathlib import Path

import onnxruntime
from piper import PiperVoice, SynthesisConfig
from piper.config import PiperConfig


def initialize(model_path, output_dir):
    global voice, config, folder
    options = onnxruntime.SessionOptions()
    options.intra_op_num_threads = 1
    options.inter_op_num_threads = 1
    voice = PiperVoice(
        session=onnxruntime.InferenceSession(model_path, sess_options=options, providers=['CPUExecutionProvider']),
        config=PiperConfig.from_dict(json.loads(Path(model_path + '.json').read_text())),
    )
    config = SynthesisConfig(length_scale=1.08)
    folder = Path(output_dir)


def generate(row):
    target = folder / ('speech-' + row['id'] + '.mp3')
    if target.exists() and target.stat().st_size > 1000:
        return
    with tempfile.TemporaryDirectory(prefix='foliant-') as temp:
        wav_path = Path(temp) / 'speech.wav'
        mp3_path = Path(temp) / 'speech.mp3'
        with wave.open(str(wav_path), 'wb') as wav:
            voice.synthesize_wav(row['text'], wav, syn_config=config)
        subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', str(wav_path), '-codec:a', 'libmp3lame', '-q:a', '2', str(mp3_path)], check=True)
        target.write_bytes(mp3_path.read_bytes())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', required=True, help='Path to de_DE-thorsten-high.onnx and adjacent .json config')
    parser.add_argument('--workers', type=int, default=2)
    args = parser.parse_args()
    folder = Path(__file__).resolve().parents[1] / 'assets/foliant-audio'
    rows = json.loads((folder / 'utterances.json').read_text())
    with multiprocessing.get_context('spawn').Pool(args.workers, initializer=initialize, initargs=(args.model, str(folder))) as pool:
        for i, _ in enumerate(pool.imap_unordered(generate, rows), 1):
            if i % 25 == 0:
                print(f'{i}/{len(rows)}', flush=True)
    manifest = [dict(id=r['id'], text=r['text'], file='assets/foliant-audio/speech-' + r['id'] + '.mp3', voice='Piper · Thorsten', provider='Piper') for r in rows]
    (folder / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
