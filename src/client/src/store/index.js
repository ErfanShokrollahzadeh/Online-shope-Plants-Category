import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    products: [],
    pagination: {
      count: 0,
      next: null,
      previous: null
    },
    loading: false,
    error: null
  },
  mutations: {
    SET_PRODUCTS(state, data) {
      state.products = data.results
      state.pagination = {
        count: data.count,
        next: data.next,
        previous: data.previous
      }
    },
    SET_LOADING(state, loading) {
      state.loading = loading
    },
    SET_ERROR(state, error) {
      state.error = error
    }
  },
  actions: {
    async fetchProducts({ commit }, page = 1) {
      commit('SET_LOADING', true)
      try {
        const response = await axios.get(`/api/products/?page=${page}`)
        commit('SET_PRODUCTS', response.data)
        commit('SET_ERROR', null)
      } catch (error) {
        commit('SET_ERROR', error.message)
        commit('SET_PRODUCTS', { results: [], count: 0, next: null, previous: null })
      } finally {
        commit('SET_LOADING', false)
      }
    }
  },
  getters: {
    getProducts: state => state.products,
    isLoading: state => state.loading,
    getError: state => state.error,
    getPagination: state => state.pagination
  }
})
