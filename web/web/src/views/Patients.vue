<template>
    <div>
      <h1> Lists of patients </h1>
      <b-table striped hover :items="retrievePatients">
        <template v-slot:cell(name)="data">
          <router-link :to="`/patients/${data.index}`">
            {{ data.value }}
          </router-link>
        </template>
      </b-table>
    </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data () {
    return {
      patients: [],
      reactive: true
    }
  },
  computed: {
    ...mapState([
      'retrievePatients'
    ])
  }
}
</script>
