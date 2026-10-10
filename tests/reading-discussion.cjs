const fs=require('fs'),vm=require('vm'),assert=require('assert');
const app=fs.readFileSync('app.js','utf8'),ctx={state:{data:{}},esc:s=>String(s)};vm.createContext(ctx);
vm.runInContext(app.slice(app.indexOf('const rooms='),app.indexOf('function esc('))+fs.readFileSync('librarian.js','utf8')+';globalThis.rounds=foliantReadingRounds;globalThis.render=foliantDebateMarkup;globalThis.journal=foliantDebateJournal;',ctx);
for(let round=0;round<4;round++){assert(ctx.render().includes(`Runde ${round+1} von 4`));assert.equal(ctx.rounds[round].options.length,3);for(let choice=0;choice<3;choice++){ctx.state.data.readingDiscussion=[...Array(round)].map(()=>({choice:0})).concat({choice});assert(ctx.render().includes(ctx.rounds[round].replies[choice]));assert(ctx.journal().includes(ctx.rounds[round].options[choice]));}ctx.state.data.readingDiscussion=Array(round+1).fill({choice:0});}
assert(ctx.render().includes('Dein vorläufiges Urteil'));ctx.state.data.lesesaalTopic=1;assert(ctx.render().includes('Ist Lesen eine Frage des Willens?'));console.log('All 12 responses, round progression, conclusion and journal verified.');

const recordings=JSON.parse(fs.readFileSync('assets/foliant-audio/manifest.json','utf8'));for(const r of ctx.rounds)for(const text of [r.question,r.basis,...r.replies])assert(recordings.some(x=>x.text===text),'Missing discussion recording: '+text);console.log('All discussion questions and responses have Piper recordings.');
vm.runInContext('globalThis.reply=foliantConversationReply;globalThis.conversation=foliantConversationMarkup;',ctx);
ctx.state.data.readingConversation=[];
const first=ctx.reply('Ohne Benachrichtigungen verstehe ich denselben Absatz besser.','attention','observation');
assert(first.reply.includes('als Erfahrung ernst'));assert(first.page==='5–6');
ctx.state.data.readingConversation.push(first);
const second=ctx.reply('Trotzdem verstehe ich den Schluss nicht.','attention','objection');assert(second.reply.includes(first.text));assert(second.reply.includes('Dein Einwand'));
ctx.state.data.readingConversation.push(second);
const third=ctx.reply('Was zeigen eigentlich die Studien?','evidence','argument');assert(third.reply.includes('Aufmerksamkeit und Bildschirm'));assert(third.question.includes('Zeitraum'));
ctx.state.data.readingConversation.push(third);assert(ctx.journal().includes(third.text));assert(ctx.conversation().includes('Gesprächszug 3'));console.log('Free contributions, topic responses, memory and journal verified.');
