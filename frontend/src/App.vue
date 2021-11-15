<template>
  <div id="nav">
    Навигация: 
    <router-link to="/actors">Actors</router-link>
    <router-link to="/directors">Directors</router-link>
    <router-link to="/genres">Genres</router-link>
  </div>
  <router-view/>
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
  display: flex;
  justify-content: center;
  align-items: center;
  border-bottom: 1px solid #2c3e50;
  color: black;
  font-size: 18px;
  font-weight: bold;
  a {
    font-weight: bold;
    color: #2c3e50;
    text-decoration: none;
    margin-left: 15px;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
