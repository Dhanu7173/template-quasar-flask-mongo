import { boot } from 'quasar/wrappers'
import { authStore } from 'src/stores/auth'

const auth = authStore()

export default boot(({ app }) => {
  app.config.globalProperties.$store = {
    auth,
  }
})
