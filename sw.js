const CACHE='mundo-antonio-jr-v3';
const CORE=['./','./index.html','./style.css','./album.css','./app.js','./album.js','./games.json','./jogar.html','./manifest.webmanifest','./icon.svg','./jogos/novos-jogos.html'];

self.addEventListener('install',event=>{
  event.waitUntil(caches.open(CACHE).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()));
});

self.addEventListener('activate',event=>{
  event.waitUntil(
    caches.keys()
      .then(keys=>Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k))))
      .then(()=>self.clients.claim())
  );
});

async function networkFirst(request){
  try{
    const response=await fetch(request);
    if(response && response.ok){
      const copy=response.clone();
      caches.open(CACHE).then(c=>c.put(request,copy));
    }
    return response;
  }catch(_){
    const cached=await caches.match(request);
    if(cached) return cached;
    throw _;
  }
}

self.addEventListener('fetch',event=>{
  if(event.request.method!=='GET') return;
  const url=new URL(event.request.url);
  if(url.origin!==location.origin) return;

  // HTML, catálogo, scripts e jogos devem buscar a versão nova primeiro.
  // Se estiver offline, o cache continua funcionando como fallback.
  const updateSensitive = event.request.mode==='navigate' || /\.(?:html|js|css|json|b64)$/.test(url.pathname);
  if(updateSensitive){
    event.respondWith(networkFirst(event.request));
    return;
  }

  event.respondWith(
    caches.match(event.request).then(cached=>cached||fetch(event.request).then(response=>{
      if(response && response.ok){
        const copy=response.clone();
        caches.open(CACHE).then(c=>c.put(event.request,copy));
      }
      return response;
    }))
  );
});
