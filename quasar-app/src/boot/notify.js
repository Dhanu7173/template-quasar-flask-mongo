import { boot } from 'quasar/wrappers'
import { Notify } from 'quasar'

Notify.setDefaults({
  position: 'top-right',
  timeout: 2500,
  textColor: 'white',
  progress:true,
  actions: [{ icon: 'close', color: 'white' }]
})

Notify.registerType('login-required', {
  message:"This feature is only available to registered users. Please log in to continue.",
  position: 'center',
  timeout: 5000,
  icon: 'announcement',
  progress: true,
  color: 'blue-8',
  textColor: 'white',
  classes:'text-bold'
})
