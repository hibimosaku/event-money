<template>
  <div>testaa</div>
</template>
<script>
import { useStore } from 'vuex'
import { key } from './store/store'
const axios = require('axios').default;

export default({
  setup() {
    const store = useStore(key)

    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/event/',
      // data: {
      //   firstName: 'Fred',
      //   lastName: 'Flintstone'
      // }
    })
      .then((res)=>{
        console.log('axios',res.data)
      })
    console.log('store',store.state.count)


  },
})
</script>