<template>
  <div>
    <h1> Lists of patients </h1>
    <ul class="list-group">
      <li class="list-group-item"
        :class="{ active: index == currentIndex }"
        v-for="(patient, index) in patients"
        :key="index"
        @click="setActivePatient(patient, index)"
      >
      </li>
    </ul>
  </div>
</template>

<script>
import PatientDataService from '../services/patientDataService'

export default {
  name: 'retrievePatients',
  data () {
    return {
      patients: [],
      currentIndex: -1
    }
  },
  methods: {
    retrievePatients () {
      PatientDataService.getAll()
        .then(res => {
          console.log(res)
          console.log(res.data)
        })
        .catch(err => {
          console.log('Something is wrong')
          console.log(err)
        })
    },
    refreshList () {
      this.retrievePatients()
      this.currentIndex = -1
    },
    setActiveTutorial (index) {
      this.currentIndex = index
    },
    mounted () {
      this.retrievePatients()
    }
  }
}
</script>
