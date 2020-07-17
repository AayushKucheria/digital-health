<template>
    <div>
      <h1> Lists of patients </h1>
        <b-table striped hover :items="patients">
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
  name: 'patients',
  mounted () {
    this.$store.dispatch('loadPatients')
  },
  computed: {
    ...mapState([
      'patients'
    ])
  }
}
</script>
