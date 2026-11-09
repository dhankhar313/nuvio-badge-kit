import fs from 'fs';
const {pats, cases} = JSON.parse(fs.readFileSync('_tests.json','utf8'));
let compileErr = 0;
const R = pats.map(({id,p}) => { let f=''; if (p.startsWith('(?i)')) { f='i'; p=p.slice(4); }
  try { return [id, new RegExp(p, f)]; } catch(e) { compileErr++; console.log('COMPILE', id, e.message); return [id, null]; } });
let bad = 0;
for (const [t, exp] of cases) {
  const h = R.filter(([id,r]) => r && r.test(t)).map(([id]) => id).sort();
  const miss = exp.filter(x => !h.includes(x)), extra = h.filter(x => !exp.includes(x));
  if (miss.length || extra.length) { bad++; console.log('JS', t, '\n  missing', miss, '\n  extra', extra); }
}
console.log('js compile errors:', compileErr, ' js failures:', bad, 'of', cases.length);
