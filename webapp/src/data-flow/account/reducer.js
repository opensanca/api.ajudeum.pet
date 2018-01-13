import { ListReducer } from 'obsidian';

import {
    FETCHING_ACCOUNT,
    FETCHING_ACCOUNT_SUCCESS,
    FETCHING_ACCOUNT_FAIL,
} from './constant';

export default ListReducer([
    FETCHING_ACCOUNT,
    FETCHING_ACCOUNT_SUCCESS,
    FETCHING_ACCOUNT_FAIL,
]);