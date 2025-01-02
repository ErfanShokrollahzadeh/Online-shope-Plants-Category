import { createStore } from 'vuex'

export default createStore({
  state: {
    products: [],
    cart: []
  },
  mutations: {
    setProducts(state, products) {
      state.products = products
    },
    addToCart(state, product) {
      state.cart.push(product)
    }
  },
  actions: {
    async fetchProducts({ commit }) {
      try {
        const response = await fetch('http://localhost:8000/api/products/')
        const data = await response.json()
        commit('setProducts', data)
      } catch (error) {
        console.error('Error fetching products:', error)
      }
    }
  }
})
