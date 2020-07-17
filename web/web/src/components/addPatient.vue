<template>
  <div class="addPatient">
    <div v-if="!submitted">
      <b-form-group id="input-group-1" label="Patient's Name:" label-for="input-1">
        <b-form-input
          id="input-1"
          type="text"
          v-model="patient.name"
          required
          placeholder="Enter patient name"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Patient's Age:" label-for="input-2">
        <b-form-input
          id="input-2"
          type="number"
          v-model="patient.age"
          required
          placeholder="Enter patient age"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Gender:" label-for="input-3">
        <b-form-select
          id="input-3"
          type="text"
          v-model="patient.sex"
          :options="['male', 'female']"
          required
        ></b-form-select>
      </b-form-group>

      <button @click="savePatient" class="btn btn-success">Submit</button>
    </div>
    <div v-else>
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" @click="newTutorial">Add</button>
    </div>
  </div>
</template>

<script>
import PatientDataService from '../services/patientDataService'

export default {
  name: 'addPatient',
  data () {
    return {
      patient: {
        id: null,
        name: '',
        sex: null,
        age: 0
      },
      submitted: false
    }
  },
  methods: {
    savePatient () {
      var data = {
        name: this.patient.name,
        sex: this.patient.sex,
        age: this.patient.age
      }
      PatientDataService.create(data)
        .then(res => {
          this.patient.id = res.data.id
          console.log(res.data.id)
          console.log(res.data)
          this.submitted = true
        })
        .catch(err => {
          console.log(err)
        })
    },
    newTutorial () {
      this.submitted = false
      this.tutorial = {}
    }
  }
}
</script>
