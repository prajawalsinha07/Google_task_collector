// Tasks.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';
import Tasks from './Tasks';

test('renders Tasks component', () => {
  const mockTasks = [{ id: 1, title: 'Test Task' }, { id: 2, title: 'Another Task' }];
  render(<Tasks tasks={mockTasks} />);
  // Check if tasks are rendered
  expect(screen.getByText(/Test Task/i)).toBeInTheDocument();
  expect(screen.getByText(/Another Task/i)).toBeInTheDocument();
});
