import Vue from 'vue'
import VueRouter from 'vue-router'
import addPatient from '../components/addPatient.vue'
import Patients from '../components/Patients.vue'
import Patient from '../components/Patient.vue'
import DLearn from '../components/DLearn.vue'
import KMean from '../components/KMean.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/addPatient',
    name: 'addPatient',
    component: addPatient
  },
  {
    path: '/',
    alias: '/patients',
    name: 'Patients',
    component: Patients
  },
  {
    path: '/patients/:id',
    name: 'Patient',
    component: Patient
  },
  {
    path: '/patients/:id/dlearn',
    name: 'DLearn',
    component: DLearn
  },
  {
    path: '/patients/:id/kmean',
    name: 'KMean',
    component: KMean
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
