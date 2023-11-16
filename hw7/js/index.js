window.addEventListener('load', () => {
  let supported = checkWorkerAndPushManager()
  if (supported){
    subscribe()
  };
});


function urlBase64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - base64String.length % 4) % 4);
  const base64 = (base64String + padding)
    .replace(/-/g, '+')
    .replace(/_/g, '/');
  const rawData = window.atob(base64);
  const outputArray = new Uint8Array(rawData.length);
  for (let i = 0; i < rawData.length; i++) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray;
}

function checkWorkerAndPushManager () {
  if (!('serviceWorker' in navigator)) {
      console.log('Workers are not supported.');
      return false;
  }
  if (!('PushManager' in window)) {
      console.log('Push notifications are not supported.');
      return false;
  }
  return true
}


async function registerServiceWorker() {
  return navigator.serviceWorker.register('js/sw.js')
  .then(function(registration) {
    console.log('Service worker successfully registered.');
    return registration;
  })
  .catch(function(err) {
    console.error('Unable to register service worker.', err);
  });
}


async function subscribe() {
  try {
    // register SW
    const registration = await registerServiceWorker();
    
    // get vapid key from server
    const response = await fetch('/get-vapid', {mode:"no-cors"});
    const publicKey = await response.text(); 

    // subscribe and send subscription to server
    const subscription = await registration.pushManager.subscribe({
      userVisibleOnly: true,
      applicationServerKey: urlBase64ToUint8Array(publicKey),
      });

    const subscribeResponse = await fetch('/send-sub', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(subscription),
      mode:"no-cors"
    });

  } catch (error) {
    console.error('Unable to get notifications: ', error);
  }
}
