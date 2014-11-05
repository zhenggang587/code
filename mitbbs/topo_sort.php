<?php

function buildHeap(&$arr) {
    for ($i = count($arr) / 2 - 1; $i >= 0; $i--) {
       siftDown($arr, $i, count($arr));
    }
}

function siftDown(&$arr, $index, $n) {
    $i = $index;
    $j = 2 * $i + 1;
    while ($j < $n) {
        if ($j + 1 < $n && $arr[$j + 1] > $arr[$j]) {
            $j++;
        }
        if ($arr[$i] >= $arr[$j]) {
            break;
        }
        $temp = $arr[$i];
        $arr[$i] = $arr[$j];
        $arr[$j] = $temp;
        $i = $j;
        $j = 2 * $i + 1;
    }
}

function heapSort(&$arr) {
    buildHeap($arr);
    $n = count($arr);
    while ($n > 0) {
        $temp = $arr[0];
        $arr[0] = $arr[$n - 1];
        $arr[$n - 1] = $temp;
        siftdown($arr, 0, --$n);
    }
}

$arr = array(3, 1, 2, 5, 4);
heapSort($arr);
print_r($arr);
