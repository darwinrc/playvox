<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <PlayvoxUserList msg="Welcome to Playvox Users"/>
  </div>
</template>

<script>
import PlayvoxUserList from './components/PlayvoxUserList.vue'

export default {
  name: 'app',
  components: {
    PlayvoxUserList
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
</style>
