import Vue from 'vue';
import Router from 'vue-router';
import PlayvoxUserList from './components/PlayvoxUserList.vue';
import PlayvoxUserNotes from './components/PlayvoxUserNotes.vue';

Vue.use(Router);

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: PlayvoxUserList
        },
        {
            path: '/notes?user=:user_id&username=:user_name',
            name: 'notes',
            component: PlayvoxUserNotes,
            props: true
        }
    ]
});

export default router;
