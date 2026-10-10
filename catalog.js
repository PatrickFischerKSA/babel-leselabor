'use strict';
let gutenbergCatalog=null;
const loadGutenberg=()=>gutenbergCatalog||(gutenbergCatalog=fetch('assets/gutenberg-catalog.json').then(r=>{if(!r.ok)throw Error('Katalog nicht erreichbar');return r.json()}));
