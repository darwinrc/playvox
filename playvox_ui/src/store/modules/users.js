import router from '@/router';

const state = {
    user: null
};

const getters = {};

const mutations = {
    setUser(state, payload) {
        state.user = payload;
    }
};

const actions = {};

export default {
    state,
    getters,
    mutations,
    actions
};
