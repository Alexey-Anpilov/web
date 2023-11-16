// Register event listener for the 'push' event.
self.addEventListener('push', function(event) {
    // Keep the service worker alive until the notification is created.
    var message = JSON.parse(event.data.text());
    event.waitUntil(
      // Show a notification with title 'ServiceWorker Cookbook' and body 'Alea iacta est'.
      self.registration.showNotification(message.title, {
        body: message.body,
      })
    );
  });
  