import React from 'react';

function ErrorMessage({ message }) {
  if (!message) return null;
  return <p className="text-red-500 text-sm">{message}</p>;
}

export default ErrorMessage;
# Add console.error for client-side errors
Enhance error display with custom component
