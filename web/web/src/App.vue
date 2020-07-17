<template>
  <div id="app">
    <div id="nav">
      <router-link to="/patients">Patient List</router-link> |
      <router-link to="/addPatient">Add Patient</router-link>
    </div>
    <b-container>
      <router-view/>
    </b-container>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #3c6dd6;
    }
  }
}
</style>

<script>
export default {
  name: 'app'
}
</script>
