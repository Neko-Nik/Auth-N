# Required features:

- [ ] Register a new user
- [ ] Login
- [ ] Logout
- [ ] Delete user
- [ ] Update user information
- [ ] Get user information
- [ ] User should be of a specific role
    - [ ] Apex Team: Internal Team who has access to all the features
    - [ ] Alliance Team: Our partners that can add / create / delete super admins under them
    - [ ] Super Admin: Can add / create / delete Admins and Users under them
    - [ ] Admin: Has some level of restriction to the super admin features (Highly customizable)
    - [ ] Standard Users: Will have access to the features that are assigned to them by the super admin or admin
- [ ] Password policy should be enforced
- [ ] User should be able to reset password
- [ ] User should be able to change password
- [ ] User should be able to change email
- [ ] User should be able to change phone number
- [ ] User should be able to change profile picture
- [ ] User should be able to change profile information
- [ ] JWT Token should be used for authentication
- [ ] JWT Token should be refreshed after a certain period of time
- [ ] Revoking JWT Token should be possible
- [ ] API Key based authentication for the Machine to Machine communication
- [ ] User should be able to see the list of users under them (if they have any)
- [ ] IP based restriction for the user
- [ ] Cross-Site Request Forgery (CSRF) protection
- [ ] Cross-Origin Resource Sharing (CORS) protection
- [ ] Passwordless login using OTP from email or SMS
- [ ] 2FA using TOTP or HOTP or U2F or WebAuthn or SMS or Email
- [ ] User should be able to see the list of devices / sessions that are logged in
- [ ] User should be able to logout from desired devices or all devices at once, nothing but revoking the JWT Token
- [ ] Account lockout after a certain number of failed login attempts
- [ ] Audit logs for the user actions
- [ ] Multi tenancy support (Single DB, Multiple Schema or Multiple DB, Multiple Schema)
- [ ] User should be able to see the list of roles that are available in the system
- [ ] User should be able to see the list of permissions that are available in the system


# Database Schema

The database (PostgreSQL) schema for the user management system will consist of the following tables:

## Tables:

1. **Users:**
    - user_id (Primary Key)
    - username
    - password_hash
    - email
    - phone_number
    - profile_picture_url
    - last_login
    - is_active
    - is_locked
    - lockout_time
    - created_at
    - updated_at
    - password_last_changed

2. **Roles:**
    - role_id (Primary Key)
    - role_name
    - description
    - created_at

3. **Permissions:**
    - permission_id (Primary Key)
    - permission_name
    - description
    - created_at
    - updated_at
    - permission_data (JSON) - for storing key-value pairs of additional data

4. **User_Roles:**
    - user_id (Foreign Key to Users)
    - role_id (Foreign Key to Roles)
    - assigned_by (Foreign Key to Users)
    - assigned_at

5. **Role_Permissions:**
    - role_id (Foreign Key to Roles)
    - permission_id (Foreign Key to Permissions)
    - assigned_by (Foreign Key to Users)
    - assigned_at

6. **Login_Attempts:**
    - attempt_id (Primary Key)
    - user_id (Foreign Key to Users)
    - attempt_time
    - success (Boolean)
    - ip_address
    - other_info (JSON) - for storing additional data

7. **Audit_Logs:**
    - log_id (Primary Key)
    - user_id (Foreign Key to Users)
    - action_performed - (e.g., login, logout, update_profile)
    - timestamp
    - details (JSON) - for storing additional data

8. **Sessions:**
    - session_id (Primary Key)
    - user_id (Foreign Key to Users)
    - device_info
    - login_time
    - last_activity_time
    - is_active

9. **JWT_Tokens:**
    - token_id (Primary Key)
    - user_id (Foreign Key to Users)
    - token
    - expiration_time

10. **API_Keys:**
    - key_id (Primary Key)
    - user_id (Foreign Key to Users)
    - key
    - created_at

11. **Password_Reset_Tokens:**
    - token_id (Primary Key)
    - user_id (Foreign Key to Users)
    - token
    - expiration_time

12. **IP_Restrictions:**
    - restriction_id (Primary Key)
    - user_id (Foreign Key to Users)
    - ip_address - (list of allowed or restricted IP addresses)
    - restriction_type - (allow or deny)
    - created_at
    - updated_at

13. **CSRF_Tokens:**
    - token_id (Primary Key)
    - user_id (Foreign Key to Users)
    - token
    - expiration_time

14. **OTP_Tokens:**
    - token_id (Primary Key)
    - user_id (Foreign Key to Users)
    - token
    - expiration_time

15. **Device_List:**
    - device_id (Primary Key)
    - user_id (Foreign Key to Users)
    - device_info
    - last_login


### Relationships:

- **Users** and **Roles** have a many-to-many relationship through the **User_Roles** table
- **Roles** and **Permissions** also have a many-to-many relationship through the **Role_Permissions** table
- **Users** are related to **Login_Attempts**, **Audit_Logs**, **Sessions**, **JWT_Tokens**, **API_Keys**, **Password_Reset_Tokens**, **IP_Restrictions**, **CSRF_Tokens**, **OTP_Tokens**, **Device_List**, and **Account_Lockout_Logs** through foreign key relationships
- **Roles** are assigned to users through the **User_Roles** table
- **Permissions** are associated with roles via the **Role_Permissions** table

### Complex Features:

- **Password Policy:** Not represented directly in the schema, but enforced in the application logic
- **JWT Token:** Stored in the **JWT_Tokens** table
- **JWT Token Refresh:** Expiration time is handled in the **JWT_Tokens** table
- **Revoking JWT Token:** Deleting records from the **JWT_Tokens** table
- **API Key Authentication:** Stored in the **API_Keys** table
- **IP-based Restriction:** Stored in the **IP_Restrictions** table
- **CSRF Protection:** Handled in the application logic, CSRF tokens stored in the **CSRF_Tokens** table
- **Passwordless Login:** OTP tokens stored in the **OTP_Tokens** table
- **2FA:** OTP tokens stored in the **OTP_Tokens** table
- **List of Devices/Sessions:** Stored in the **Device_List** table
- **Logout from Devices:** Removing records from the **Device_List** table
- **Account Lockout:** Account lockout logs stored in the **Account_Lockout_Logs** table
- **Audit Logs:** Stored in the **Audit_Logs** table
- **Multi-Tenancy:** Not represented in the schema, but can be implemented using a multi-tenant architecture


# API Endpoints

1. **Authentication and Authorization Endpoints**:
   - `/register` (POST): Register a new user
   - `/login` (POST): Login
   - `/logout` (POST): Logout
   - `/refresh-token` (POST): Refresh JWT token
   - `/forgot-password` (POST): Initiate password reset (passwordless login)
   - `/reset-password` (POST): Reset password
   - `/change-password` (POST): Change password
   - `/change-email` (POST): Change email
   - `/change-phone-number` (POST): Change phone number
   - `/change-profile-picture` (POST): Change profile picture
   - `/change-profile-information` (POST): Change profile information

2. **User Management Endpoints**:
   - `/users` (GET): Get user information (current user)
   - `/users/{user_id}` (GET): Get user information (by ID)
   - `/users/{user_id}` (PUT): Update user information
   - `/users/{user_id}` (DELETE): Delete user

3. **Role and Permission Management Endpoints**:
   - `/roles` (GET): Get list of roles
   - `/permissions` (GET): Get list of permissions
   - `/user-roles` (GET): Get list of roles assigned to the user
   - `/role-permissions` (GET): Get list of permissions assigned to the role

4. **User Relationship Endpoints**:
   - `/users/{user_id}/subordinates` (GET): Get list of users under the specified user (if applicable)
   - `/devices` (GET): Get list of devices/sessions logged in
   - `/devices/{device_id}` (DELETE): Logout from specific device
   - `/devices/logout` (POST): Logout from all devices

5. **Audit Log Endpoints**:
   - `/audit-logs` (GET): Get audit logs for user actions

6. **Account Lockout Endpoints**:
   - `/account-lockout-logs` (GET): Get account lockout logs
   - `/account-lockout-config` (GET, PUT): Get or update account lockout configuration

7. **IP Restriction Endpoints**:
   - `/ip-restrictions` (GET): Get IP restrictions for user
   - `/ip-restrictions` (POST, DELETE): Add or remove IP restriction for user

8. **CSRF Token Endpoints**:
   - `/csrf-tokens` (GET, POST): Get or generate CSRF tokens
   - `/csrf-tokens/{token_id}` (DELETE): Invalidate CSRF token

9. **API Key Endpoints**:
   - `/api-keys` (GET, POST): Get or generate API keys
   - `/api-keys/{key_id}` (DELETE): Revoke API key

10. **OTP Token Endpoints**:
    - `/otp-tokens` (POST): Generate OTP token (for passwordless login or 2FA)
    - `/otp-tokens/verify` (POST): Verify OTP token

11. **Other Endpoints**:
    - `/health` (GET): Health check endpoint


## Additional Endpoints

1. **Role and Permission Management Endpoints**:
   - `/roles` (POST): Create a new role
   - `/roles/{role_id}` (PUT): Update role information
   - `/roles/{role_id}` (DELETE): Delete a role
   - `/permissions` (POST): Create a new permission
   - `/permissions/{permission_id}` (PUT): Update permission information
   - `/permissions/{permission_id}` (DELETE): Delete a permission
   - `/users/{user_id}/roles` (GET): Get list of roles assigned to a user
   - `/users/{user_id}/roles/{role_id}` (PUT): Assign a role to a user
   - `/users/{user_id}/roles/{role_id}` (DELETE): Remove a role from a user

2. **JWT Token Management Endpoints**:
   - `/jwt-tokens/invalidate` (POST): Invalidate JWT token (force logout)
   - `/jwt-tokens` (GET): Get list of active JWT tokens for a user

3. **Session Management Endpoints**:
   - `/sessions/{session_id}` (DELETE): Invalidate a specific session
   - `/sessions` (DELETE): Invalidate all sessions for a user

4. **Password Policy Endpoints**:
   - `/password-policy` (GET): Get password policy settings
   - `/password-policy` (PUT): Update password policy settings

5. **Account Lockout Management Endpoints**:
   - `/account-lockout-config` (POST): Update account lockout configuration

6. **Audit Log Endpoints**:
   - `/audit-logs/{user_id}` (GET): Get audit logs for a specific user

7. **Multi-Tenancy Endpoints**:
   - `/tenants` (GET): Get list of tenants
   - `/tenants/{tenant_id}` (GET): Get details of a specific tenant
   - `/tenants/{tenant_id}/users` (GET): Get list of users belonging to a specific tenant
   - `/tenants/{tenant_id}/roles` (GET): Get list of roles available for a specific tenant
   - `/tenants/{tenant_id}/permissions` (GET): Get list of permissions available for a specific tenant

8. **User Activity Tracking Endpoints**:
   - `/user-activity` (GET): Get user activity summary (login times, actions performed, etc.)

9. **User Suspension/Activation Endpoints**:
   - `/users/{user_id}/suspend` (POST): Suspend a user account
   - `/users/{user_id}/activate` (POST): Activate a suspended user account

10. **User Search Endpoints**:
    - `/users/search` (GET): Search for users based on criteria such as username, email, phone number, etc.

11. **API Documentation Endpoints**:
    - `/documentation` (GET): Retrieve API documentation

12. **User Import/Export Endpoints**:
    - `/users/import` (POST): Import users from a file
    - `/users/export` (GET): Export user data to a file
