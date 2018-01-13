import { ListReducer } from 'obsidian';

import {
    FETCHING_ADOPTION,
    FETCHING_ADOPTION_SUCCESS,
    FETCHING_ADOPTION_FAIL,
} from './constant';

export default ListReducer([
    FETCHING_ADOPTION,
    FETCHING_ADOPTION_SUCCESS,
    FETCHING_ADOPTION_FAIL,
]);