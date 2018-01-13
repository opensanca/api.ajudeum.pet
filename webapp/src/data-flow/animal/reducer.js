import { ListReducer } from 'obsidian';

import {
    FETCHING_ANIMAL,
    FETCHING_ANIMAL_SUCCESS,
    FETCHING_ANIMAL_FAIL,
} from './constant';

export default ListReducer([
    FETCHING_ANIMAL,
    FETCHING_ANIMAL_SUCCESS,
    FETCHING_ANIMAL_FAIL,
]);