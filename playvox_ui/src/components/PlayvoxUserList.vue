<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      For a guide and recipes on how to configure / customize this project,<br>
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>
    <h3>Installed CLI Plugins</h3>
    <ul>
      <li>LISTA DE USUARIOS </li>
      <li v-for="(user, idx) in users" :key="idx">
        {{user.first_name}} 
        <!-- <a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank" rel="noopener">babel</a> -->
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PlayvoxUserList',
  props: {
    msg: String
  },
  data() {
    return {
        users: []
    };
  },
  methods: {
      listUsers() {
        axios.get('http://localhost:5000/v1/users'
        // , {
        //         // params: {
        //         //     q: plan,
        //         //     app_id: '5b6623d5',
        //         //     app_key: '46674aa2193dbb7b88ffd897331e661a',
        //         //     from: 0,
        //         //     to: 9
        //         // }
        //     }
          )
            .then(response => {
                this.users  = response.data;
                console.log(this.users);
                
            })
            .catch(() => {
                this.users = [];
            });
      }
    },
    beforeMount() {
      this.listUsers()
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
