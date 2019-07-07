<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Vuetify</span>
        <span class="font-weight-light">Watchin SGE</span>
      </v-toolbar-title>
    </v-toolbar>

    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  mounted(){
    if(this.$store.state.users.user){
      this.$router.push('/')
    }
    else{
      this.$router.push('/login')
    }
  }
}
</script>
