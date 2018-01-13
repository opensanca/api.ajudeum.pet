import client from '../api';

import {
    FETCHING_ANIMAL,
    FETCHING_ANIMAL_SUCCESS,
    FETCHING_ANIMAL_FAIL,
} from './constant';

export const getAll = () => ({
    type: [FETCHING_ANIMAL, FETCHING_ANIMAL_SUCCESS, FETCHING_ANIMAL_FAIL],
    api: client.Animal.find()
});