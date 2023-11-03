function checkWorkerAndPushManager(){
    if (!('serviceWorker') in navigator){
        return false
    }

    if (!('PushManager') in window){
        return false
    }
    return true
}


function registerServiceWorker(){
    return navigator.serviceWorker.register('js/sw.js').then(
        (registration) =>{
            console.log("Service worker successfully registered.");
            return registration
        },
        (error) => {
            console.error('Unable to register service worker.', error);
        });
}

function askPermission(){
    return new Promise(function(resolve, reject) {
        const permissionResult = Notification.requestPermission(function(result){
            resolve(result);
    });

    if (permissionResult) {
        permissionResult.then(resolve, reject);
      }
    })
    .then(function(permissionResult) {
      if (permissionResult !== 'granted') {
        throw new Error('We weren\'t granted permission.');
      }
    });
}




if (checkWorkerAndPushManager()){
    registerServiceWorker()
}