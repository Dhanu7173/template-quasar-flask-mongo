import { boot } from 'quasar/wrappers'
import TournamentCard2 from 'src/components/TournamentCard2.vue'
import LoadingComponent from 'src/components/LoadingComponent.vue'

export default boot(({ app }) => {
  app.component('loading-component', LoadingComponent)

})
