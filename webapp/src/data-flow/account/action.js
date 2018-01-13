import client from '../api';

import {
    FETCHING_ACCOUNT,
    FETCHING_ACCOUNT_SUCCESS,
    FETCHING_ACCOUNT_FAIL,
} from './constant';

export const getAll = () => ({
    type: [FETCHING_ACCOUNT, FETCHING_ACCOUNT_SUCCESS, FETCHING_ACCOUNT_FAIL],
    api: client.Account.find()
});