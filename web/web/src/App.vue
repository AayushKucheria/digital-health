<template>
  <div id="app">
    <div id="nav">
      <router-link to="/patients">Patient List</router-link> >>
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
  color: #2a3a49;
  font-size: 1em;
}

#nav {
  padding: 30px;
  background-color: rgb(218, 180, 180);;

  a {
    font-weight: bold;
    color: #2d3944;
    font-size: 1.5em;
    margin: 0 1em;

    &.router-link-exact-active {
      color: #3c6dd6;
      font-size: 1.5em;
    }
  }
}
</style>

<script>
export default {
  name: 'app'
}
</script>
