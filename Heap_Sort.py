{
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "\n",
        "import timeit\n",
        "import random\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "# Heapify function to maintain the heap property\n",
        "def heapify(arr, n, i):\n",
        "    largest = i\n",
        "    left = 2 * i + 1\n",
        "    right = 2 * i + 2\n",
        "\n",
        "    if left < n and arr[i] < arr[left]:\n",
        "        largest = left\n",
        "\n",
        "    if right < n and arr[largest] < arr[right]:\n",
        "        largest = right\n",
        "\n",
        "    if largest != i:\n",
        "        arr[i], arr[largest] = arr[largest], arr[i]\n",
        "        heapify(arr, n, largest)\n",
        "\n",
        "# Heap Sort function\n",
        "def heapSort(arr):\n",
        "    n = len(arr)\n",
        "    # Build a max heap\n",
        "    for i in range(n//2 - 1, -1, -1):\n",
        "        heapify(arr, n, i)\n",
        "\n",
        "    # One by one extract elements from the heap\n",
        "    for i in range(n-1, 0, -1):\n",
        "        arr[i], arr[0] = arr[0], arr[i]  # Swap\n",
        "        heapify(arr, i, 0)\n",
        "\n",
        "# Test data and timing setup\n",
        "list_lengths = [10000, 20000, 30000, 50000, 60000]\n",
        "time_taken = []\n",
        "\n",
        "# Loop to measure the time taken for different list sizes\n",
        "for length in list_lengths:\n",
        "    # Generate a random list of the current length\n",
        "    arr = [random.randint(1, 100000) for _ in range(length)]\n",
        "\n",
        "    # Measure the time taken to sort the list using heapSort\n",
        "    setup_code = \"from __main__ import heapSort\"\n",
        "    test_code = f\"heapSort({arr})\"\n",
        "\n",
        "    # Measure the execution time\n",
        "    execution_time = timeit.timeit(test_code, setup=setup_code, number=1)\n",
        "    time_taken.append(execution_time)\n",
        "\n",
        "# Plotting the results\n",
        "plt.plot(list_lengths, time_taken)\n",
        "plt.xlabel('Size of array')\n",
        "plt.ylabel('Time taken (seconds)')\n",
        "plt.title('Time Complexity of Heap Sort')\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "c5atBsAK93YM"
      },
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "name": "Welcome To Colab",
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
