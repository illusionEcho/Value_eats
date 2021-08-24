import Vue from 'vue';
import Layout from './components/Layout';
import router from './routers/eateryRouter';
import { rootStore } from './stores/rootStore';
import './common/bootstrap';

rootStore.mode = 'eatery';

new Vue({
  router,
  render: h => h(Layout, [h('router-view')]),
}).$mount('#app');

