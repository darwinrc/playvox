<template>
  <div>
    <h1>Users</h1>
     <v-data-table
      :headers="headers"
      :items="users"
      class="elevation-1"
      hide-actions
    >
    <template v-slot:items="props">
      <router-link tag="tr" 
        :to="{ name: 'notes', params: { user_id: props.item._id, user_name: `${props.item.first_name} ${props.item.last_name}` }}">
        <td class="text-md-left">{{ props.item.first_name }} {{ props.item.last_name }}</td>
        <td class="text-md-left">{{ props.item.email }}</td>
        <td class="text-md-left">{{ props.item.age }}</td>
        <td class="text-md-left">{{ props.item.sex }}</td>
      </router-link>
    </template>
  </v-data-table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PlayvoxUserList',
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
            })
            .catch((e) => {
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
