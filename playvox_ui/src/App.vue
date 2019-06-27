<template>
  <div id="app">
    <img class="playvox-logo" alt="Playvox logo" src="./assets/playvox_logo.png">
    <router-view></router-view>
  </div>
</template>

<script>
import PlayvoxUserList from './components/PlayvoxUserList.vue'
import PlayvoxUserNotes from './components/PlayvoxUserNotes.vue'

export default {
  name: 'app',
  components: {
    PlayvoxUserList,
    PlayvoxUserNotes
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.playvox-logo {
  width: 33%;
}
</style>
