```markdown
# jiaruo Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches the core development patterns and conventions used in the `jiaruo` TypeScript codebase. You'll learn how to structure files, write imports/exports, and follow the project's conventions for naming and testing. This guide also provides step-by-step workflows and handy commands to streamline your development process.

## Coding Conventions

### File Naming
- **Style:** kebab-case
- **Example:**  
  ```
  user-profile.ts
  data-fetcher.test.ts
  ```

### Imports
- **Style:** Relative imports
- **Example:**
  ```typescript
  import { fetchData } from './data-fetcher';
  ```

### Exports
- **Style:** Named exports
- **Example:**
  ```typescript
  // In user-profile.ts
  export function getUserProfile(id: string) { ... }
  ```

### Commit Messages
- **Pattern:** Freeform, no strict prefixes
- **Average Length:** ~32 characters

## Workflows

### Adding a New Module
**Trigger:** When you need to create a new feature or utility module  
**Command:** `/add-module`

1. Create a new `.ts` file using kebab-case for the filename.
2. Implement your logic using named exports.
3. Use relative imports for any dependencies.
4. If applicable, create a corresponding `.test.ts` file for tests.

### Writing Tests
**Trigger:** When you add or update functionality  
**Command:** `/write-test`

1. Create a test file with the pattern `*.test.ts` (kebab-case).
2. Write tests using the project's preferred (unknown) testing framework.
3. Use relative imports to bring in the module under test.
4. Run your tests using the project's test runner.

### Refactoring Imports/Exports
**Trigger:** When organizing or cleaning up code  
**Command:** `/refactor-imports-exports`

1. Ensure all imports are relative (e.g., `./module`).
2. Use named exports exclusively.
3. Update any import statements in dependent files.

## Testing Patterns

- **File Pattern:** All test files use the `*.test.ts` naming convention and kebab-case.
- **Framework:** The specific testing framework is unknown, but tests are colocated with source files or in the same directory.
- **Example:**
  ```typescript
  // data-fetcher.test.ts
  import { fetchData } from './data-fetcher';

  describe('fetchData', () => {
    it('should return data', () => {
      // test implementation
    });
  });
  ```

## Commands
| Command                   | Purpose                                         |
|---------------------------|-------------------------------------------------|
| /add-module               | Scaffold a new module with proper conventions   |
| /write-test               | Create a test file for a module                 |
| /refactor-imports-exports | Standardize imports and exports in a file       |
```
