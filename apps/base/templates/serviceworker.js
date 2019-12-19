var filesToCache = [
    '/',
    '/listas',
    '/productos',
    '/tiendas',
    '/login',
    '/registro',
];

var staticCacheName = 'misperris-v1';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '/'
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
      event.respondWith(      
        caches.open(staticCacheName).then(function(cache) {
          return cache.match(event.request).then(function(response) {
            var fetchPromise = fetch(event.request).then(function(networkResponse) {
              cache.put(event.request, networkResponse.clone());
              return networkResponse;
            })
            return response || fetchPromise;
          })
        })
      );
  });
