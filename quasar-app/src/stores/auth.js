import {defineStore} from 'pinia';

export const authStore = defineStore('auth', {
  state: () => ({
    login_status: false,
    _id: '',
    username: 'No username',
    avatar: null,
    is_profile_complete: false,
  }),
  getters: {
    isLoggedIn:(state)=> state.login_status,
    getAvatar:(state)=> state.avatar,
    getUsername:(state)=> state.username || "No username",
  },
  actions: {
    setSession(data) {
      this.login_status = true
      this._id = data._id
      this.username = data.username
      this.avatar = data.avatar
      this.is_profile_complete = data.is_profile_complete
    },
    unsetSession() {
      this.login_status = false
      this._id = ''
      this.username = 'No username'
      this.avatar = null
      this.is_profile_complete = false
    },
  },
});
