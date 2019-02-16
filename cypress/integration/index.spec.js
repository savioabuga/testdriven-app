describe('Index', () => {
  it('users should be able to view "/" page', () => {
    cy.visit('/').get('h1').contains('All Users');
  })
})
