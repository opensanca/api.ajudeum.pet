import client from '../api';

import {
    FETCHING_ADOPTION,
    FETCHING_ADOPTION_SUCCESS,
    FETCHING_ADOPTION_FAIL,
} from './constant';

export const getAll = () => ({
    type: [FETCHING_ADOPTION, FETCHING_ADOPTION_SUCCESS, FETCHING_ADOPTION_FAIL],
    api: client.Adoption.find()
});