<template>
  <v-app>
    <v-navigation-drawer
      v-if="$route.name != 'login'"
      v-model="drawer"
      fixed
      clipped
      app
    >
      <v-list class="pt-0" dense>

        <v-list-tile
          v-for="item in items"
          :key="item.title"
          @click=""
        >
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <router-link :to="item.url">
              <v-list-tile-title>{{ item.title }}</v-list-tile-title>
            </router-link>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar app fixed>
      <v-toolbar-side-icon 
        v-if="$route.name != 'login'" 
        @click.stop="drawer = !drawer"
      ></v-toolbar-side-icon>
      <v-toolbar-title class="headline text-uppercase">
        <span>Watchin</span>
        <span class="font-weight-light">SGE</span>
      </v-toolbar-title>
    </v-toolbar>
    <v-snackbar
      v-model="$store.state.snackbar.value"
      :color="$store.state.snackbar.type"
      top="true"
    >
      {{ $store.state.snackbar.text }}
    </v-snackbar>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import "./App.css";

export default {
  name: 'App',
  data(){
    return {
      drawer: false,
      items: [
        {icon:'home', title: 'home', url: "/home"}
      ]
    }
  },
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
