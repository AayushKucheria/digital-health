<template>
    <div>
      <h1> Lists of patients </h1>
        <b-table striped hover
        :items="patients">
          <template v-slot:cell(name)="data">
            <router-link :to="`/patients/${data.index}`">
              {{ data.value }}
            </router-link>
          </template>
        </b-table>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'patients',
  data () {
    return {
      patient: {
        sex: '',
        age: 0,
        name: '',
        id: 0
      }
    }
  },
  methods: {
    ...mapActions([
      'loadPatients',
      'loadPatient'
    ])
  },
  computed: {
    ...mapState([
      'patients'
    ])
  },
  created () {
    this.loadPatients()
    // this.loadPatient(0)
  }
}
</script>
