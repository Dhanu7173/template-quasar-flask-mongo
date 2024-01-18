import { authStore } from "src/stores/auth";
import { api } from "src/boot/axios";

export const auth_guard = (to, from, next) => {
  const auth_store = authStore()
  const to_flag = to.path == '/login'
  const route_to = (route1=undefined, route2=undefined)=>{
    if(to_flag){
      (route1 && (next(route1) || true)) || next()
    }else{
      (route2 && (next(route2) || true)) || next()
    }
  }
  if(auth_store.isLoggedIn){
    route_to('/',undefined)
  }else{
    if(to.meta.requiresAuth || to_flag){
      api.get('/auth/').then(response=>{
        if(response.data.ok){
          auth_store.setSession(response.data.user_data)
          route_to('/',undefined)
        }else{
          route_to(undefined,'/login')
        }
      }).catch(error=>{
        console.error(error)
        next('/login')
      })
    }else{
        next()
    }
  }
}
