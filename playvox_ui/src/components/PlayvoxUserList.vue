<template>
  <div>
    <h1>Users</h1>
     <v-data-table
      :headers="headers"
      :items="users"
      class="elevation-1"
      hide-actions
    >
    <template slot="headers">
        <tr>
          <th
            v-for="header in headers"
            :key="header.text">
            {{ header.text }}
          </th>
        </tr>
        <tr class="grey lighten-3">
          <th
            v-for="header in headers"
            :key="header.text">
            <div v-if="filters.hasOwnProperty(header.value)">
              <v-text-field
                label="Filter"
                v-model=filters[header.value]
                hide-details
              ></v-text-field>
            </div>
            <div v-if="!filters.hasOwnProperty(header.value)">
              <v-btn flat color="primary" @click="applyFilters()">Apply filters</v-btn>
            </div>
          </th>
        </tr>
      </template>
    
    <template v-slot:items="props">
      <router-link tag="tr" 
        :to="{ name: 'notes', params: { user_id: props.item._id, user_name: `${props.item.first_name} ${props.item.last_name}` }}">
        <td class="text-md-left">{{ props.item.first_name }}</td>
        <td class="text-md-left">{{ props.item.last_name }}</td>
        <td class="text-md-left">{{ props.item.email }}</td>
        <td class="text-md-left">{{ props.item.sex }}</td>
        <td class="text-md-left">{{ props.item.age }}</td>
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
      search: '',
      headers: [
          {
            text: 'First Name',
            align: 'left',
            sortable: false,
            value: 'first_name'
          },
          {
            text: 'Last Name',
            align: 'left',
            sortable: false,
            value: 'last_name'
          },
          { 
            text: 'Email', 
            align: 'left',
            sortable: false,
            value: 'email' 
          },
          { 
            text: 'Sex',
            value: 'sex',
            align: 'left',
            sortable: false,
          },
          { 
            text: 'Age', 
            align: 'left',
            sortable: false,
            value: 'age' 
          }
        ],
        filters: {
          first_name: '',
          last_name: '',
          email: '',
          sex: '',
        },
        users: []
    };
  },
  methods: {
      listUsers() {
        axios.get('http://localhost:5000/v1/users').then(response => {
          this.users = response.data;    
        }).catch((e) => {
          this.users = [];
        });
      },
      applyFilters() {  
        axios.get('http://localhost:5000/v1/users', {
          params: {
              query: JSON.stringify(this.filters)
          }
        }).then(response => {
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
