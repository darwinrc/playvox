<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
     <v-data-table
      :headers="headers"
      :items="users"
      class="elevation-1"
      hide-actions
    >
    <template v-slot:items="props">
      <td class="text-md-left">{{ props.item.first_name }} {{ props.item.last_name }}</td>
      <td class="text-md-left">{{ props.item.email }}</td>
      <td class="text-md-left">{{ props.item.age }}</td>
      <td class="text-md-left">{{ props.item.sex }}</td>
    </template>
  </v-data-table>
    <!-- <ul>
      <li> </li>
      <li v-for="(user, idx) in users" :key="idx">
        <a href="#">{{user.first_name}} {{user.last_name}} {{user.sex}} {{user.email}} {{user.age}}</a> 
        <a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank" rel="noopener">babel</a> 
      </li>
    </ul> -->
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
      headers: [
          {
            text: 'User',
            align: 'left',
            sortable: false,
            value: 'name'
          },
          { 
            text: 'Email', 
            align: 'left',
            sortable: false,
            value: 'email' 
          },
          { 
            text: 'Age', 
            align: 'left',
            sortable: false,
            value: 'age' 
          },
          { 
            text: 'Sex',
            value: 'sex',
            align: 'left',
            sortable: false,
          }
        ],
        users: []
    };
  },
  methods: {
      listUsers() {
        console.log('calling endpoint');
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
                this.users = response.data;
                console.log(this.users);
                
            })
            .catch((e) => {
              console.log('error: ', e);
                this.users = [];
            });
      }
    },
    beforeMount() {
      this.listUsers();
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
td {
  cursor: pointer;
}
</style>
