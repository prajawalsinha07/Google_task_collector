// Tasks.test.js
import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import Tasks from './Tasks';

// Mocking the global fetch API
global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve([{ taskID: 1, taskDescription: 'Complete project', taskState: 'In Progress' }])
  })
);

beforeEach(() => {
  fetch.mockClear();
});

describe('Tasks Component', () => {
  it('fetches and displays tasks', async () => {
    render(<Tasks />);
    await waitFor(() => {
      // Check if the task is rendered with correct content
      expect(screen.getByText('Complete project')).toBeInTheDocument();
      expect(screen.getByText('In Progress')).toBeInTheDocument();
    });
  });

});

describe('Tasks Component Error Handling', () => {
    it('displays an error message when fetch fails', async () => {
      // Mocking a fetch failure
      global.fetch = jest.fn(() =>
        Promise.reject(new Error('API fetch failed'))
      );
  
      render(<Tasks />);
      await waitFor(() => {
        // Check for an error message
        expect(screen.getByText(/Error fetching tasks:/i)).toBeInTheDocument();
      });
    });
  });
  
