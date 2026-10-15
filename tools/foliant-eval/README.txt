Foliant browser-model comparison — protocol, 15 October 2026

Question: Does Qwen3.5 9B improve on Qwen3 8B in Foliant's current literary salon?

Design: within-device comparison. Same WebLLM 0.2.86 runtime, production system prompt and message builder, six fixed two-turn cases. Temperature 0, seed 42, 420 output-token maximum, /no_think suffix as in production. Fresh chat per case. Model order: Qwen3 8B, then Qwen3.5 9B. No prompt tuning between models. Model loading time recorded separately; cache and fixed order make load-time comparisons non-causal. Inference times are observations for this device only. One run, not a statistical benchmark.

Cases: Kafka's neutral tone versus 'ungeheuren'; an ambiguous invented letter scene; a false premise about Erlkönig; a demand for nonexistent quotation/author/page; a circular entry requirement without inferred malicious intent; an argument about summaries which must be qualified after a counterexample.

Rubric per answer (0–2 each, maximum 10):
1. Text fidelity: 0 fabricated or contradictory textual claim; 1 plausible but loose/unsupported detail; 2 precise and supported, distinguishes inference.
2. Responsiveness: 0 avoids the actual claim; 1 partially addresses it; 2 directly answers the actual claim/correction.
3. Argumentative progress: 0 repeats generic principles; 1 relevant paraphrase; 2 adds a reason, distinction, revision or discriminating test.
4. Dialogical discipline: 0 entrenches an error or ignores instruction; 1 weak acknowledgment or reflexive question; 2 appropriately concedes, qualifies or defends with reasons.
5. Language and usefulness: 0 incoherent/unusable; 1 understandable but awkward or padded; 2 clear, concise and useful for pupils.

Critical errors are recorded separately; high mean score cannot erase invented quotations or false factual assertions. Second-turn answers are primary for the repetition complaint. Human review by this assistant, unblinded; no independent grader. Do not claim significance, general superiority or reliability on all literature from this sample.

Saved output includes the full visible model answer, finish reason, token usage and timings. Internal thinking text is excluded from the research copies; only its presence and character count are retained. Finish='length' is a truncation, not necessarily a reasoning error. Original text from Goethe and Kafka is public-domain; invented passages are explicitly identified. No student data used.

Protocol amendment during pilot (recorded before the controlled second run):
The production message construction and mode hint (with fixed benchmark sampling settings) yielded two 420-token length-limited answers with no visible output from Qwen3.5 9B. Raw outputs began with an internal thinking block; a third answer was interrupted. This is an integration/mode-control failure, not evidence about literary quality. Archive: as-integrated-results.json. The first model's 12 baseline answers are preserved there too.

For the controlled rerun, BOTH models receive extra_body: {enable_thinking:false}, the WebLLM request setting, in addition to the unchanged production messages and /no_think suffix. All other settings and cases are unchanged. Evaluate this controlled pair separately. This discovers that the current production suffix alone is not a portable thinking-mode control. Do not silently conflate pilot and controlled answers or load times.
