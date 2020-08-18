<template>
  <div>
    <h1> K-Mean Result</h1>
        <b-table striped hover
        :items="results">
          <template v-slot:cell(result)="data">
            {{ data.value }}
          </template>
        </b-table>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'results',
  data () {
    return {
      result: {
        patient_id: 0,
        model_id: 0,
        result: 0,
        session_id: 0
      }
    }
  },
  methods: {
    ...mapActions([
      'loadKMResult'
    ])
  },
  computed: {
    ...mapState([
      'results'
    ])
  },
  created () {
    this.loadKMResult(this.$route.params.id)
  }
}
</script>
