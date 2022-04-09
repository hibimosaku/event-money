import { createApp } from "vue"
import router from "../src/router/router"
import { store, key } from './store/store'

const app = createApp({});
app.use(router)
app.use(store,key)
app.mount("#app");

