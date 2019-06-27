<template>
  <div>
    <h1>Notes for {{user_name}}</h1>
     <v-data-table
      :headers="headers"
      :items="notes"
      class="elevation-1"
      hide-actions
    >
    <template v-slot:items="props">
        <td class="text-md-left">{{ props.item.title }}</td>
        <td class="text-md-left">{{ props.item.body }}</td>
        <td class="text-md-left">{{ props.item.note_date }}</td>
    </template>
  </v-data-table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PlayvoxUserNotes',
  props: {
    user_id: String,
    user_name: String
  },
  data() {
    return {
      headers: [
          {
            text: 'Title',
            align: 'left',
            sortable: false,
            value: 'title'
          },
          { 
            text: 'Body', 
            align: 'left',
            sortable: false,
            value: 'body' 
          },
          { 
            text: 'Date', 
            align: 'left',
            sortable: false,
            value: 'date' 
          }
        ],
        notes: []
    };
  },
  methods: {
      getNotes() {
        axios.get(`http://localhost:5001/v1/users/${this.user_id}/notes`)
            .then(response => {
                this.notes = response.data;
            })
            .catch((e) => {
                this.notes = [];
            });
      }
    },
    beforeMount() {
      this.getNotes();
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
</style>
